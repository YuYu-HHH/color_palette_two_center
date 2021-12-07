import numpy as np
from numpy.matlib import repmat
#X,k,opt
from scipy import sparse
from scipy.sparse import spdiags


def get_max_index(A1):
    row , col = A1.shape;
    return_label = np.zeros([1,col]);
    for j in range(col):
        base_num = A1[0,j];
        base_row = 0;
        for i in range(row):
            if A1[i,j] > base_num:
                base_num = A1[i,j];
                base_row = i;
        return_label[0,j] = base_row;
    return return_label;

def fkmeans(X,k,weights):
    n = X.shape[0]
    careful = 0;
    weight = weights;

    # print(k.shape)
    if np.isscalar(k):
        if careful == 1:
            k = spreadseeds(X,k);
        if careful == 0:
            k = X[np.random(X.shape[0], k), :];

    B = np.transpose(X);
    X1 = np.dot(k,B);

    # X2 = 0.5 * np.sum(np.square(k),2);
    X2 = 0.5 * np.sum(k**2 ,axis = 1);

    mm1 = X1.shape[1];

    X3 = np.tile(X2,(mm1,1));
    X3 = np.transpose(X3);

    A1 = X1 - X3;

    label = np.argmax(A1,axis = 0);

    k = k.shape[0]
    label = np.array(label);
    # print(label.shape)
    last = [0];
    label = np.transpose(label)
    if len(weight) == 0:
        while label.any() != last.any():
            # _,__,label = np.unique(label);

            AA1 = [];
            for i in range(n):
                AA1.append(i);
            AA1 = np.array(AA1);

            ind = sparse.csr_matrix((weight, (label,AA1)), shape=(k, n), dtype=np.int32)
            centroid = (spdiags(1. / sum(ind, 2), 0, k, k) * ind) * X;
            X1 = centroid * np.transpose(X);
            X2 = 0.5*sum(centroid**2,2)
            mm1 = X1.shape[0]
            X3 = np.tile(X2,(1,mm1));
            distances = X1 - X3;
            last = label;
            _,label = max(distances);
        dis = ind * (sum(X**2,2) - 2* max(distances).T);
    else:
        last = np.array(last);
        while label.any() != last.any():
            label = np.array(label);
            AA1 = [];
            for i in range(0, n):
                AA1.append(i);
            AA1 = np.array(AA1);

            ind = sparse.csr_matrix((weight, (label, AA1)), shape=(k, n), dtype=np.int32)

            sum = 0;
            for i in ind:
                sum = sum + i;

            weights_new = (spdiags((1 / np.sum(ind, axis=1)).transpose(), 0, k, k) * ind);

            centroid = (spdiags((1 / np.sum(ind, axis = 1)).transpose(), 0, k, k) * ind) * X;

            centroid = np.array(centroid)
            # print(centroid.shape)
            X1 = np.dot(centroid , np.transpose(X));
            X2 = 0.5 * np.sum(centroid ** 2, axis = 1)
            mm1 = X1.shape[1];
            X3 = np.tile(X2, (mm1,1));
            X3 = np.transpose(X3);
            distances = X1 - X3;

            last = label;
            label = np.argmax(distances,axis = 0);
            label = np.transpose(label);

        dis = ind * (np.sum(X ** 2,axis = 1) - 2 * np.transpose(np.max(distances,axis = 0)));
    label = label.T;

    #A.dia 越小，占比越大
    return label,centroid ,dis;


def spreadseeds(X,k):
    n,d = np.size(X);
    idx = np.zeros(k,1);
    S = np.zeros(k,d);
    D = np.inf(n, 1);
    idx[1] = np.ceil(n*np.rand(0,1));
    S[1,:] = X[idx[1],:];
    for i in range(2,k):
        D = min(D,sqrdistance(S[i-1,:],X));
        idx[i] = np.where(np.cumsum(D)/sum(D > np.rand(0,1)),1);
        S[i,:] = X[idx[i],:];
    return S,idx;


def sqrdistance(A,B):
    n1 = np.size(A,1);
    n2 = np.size(B,2);
    m = (sum(A,1) + sum(B,1))/(n1+n2);
    # A = bsxfun
    A1 = repmat(m, n1);
    A = A - A1;
    B1 = repmat(m,n2);
    B = B - B1;
    D = np.full((-2)*A * np.transpose(B));
    D1 = repmat(np.full(sum(np.power(B,2),2)));
    D = D + D1;
    D2 = repmat(np.full(sum(np.power(A, 2), 2)));
    D = D + D2;

    return D;



