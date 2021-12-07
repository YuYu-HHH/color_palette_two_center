import math
import numpy as np
from get_the_picture_about_color.fkmeans import fkmeans
from get_the_picture_about_color.rgblab import rgb2lab_matrix, lab2rgb_matrix

def extract_theme(I,k,sigma,discard_black):
    bin = 64;
    I = np.asarray(I)
    h,w,c = I.shape;
    I = np.array(I)
    if discard_black == 1:
        k = k + 1;

    Ibin = np.zeros([h,w,c]);
    for i in range(h):
        for j in range(w):
            for t in range(c):
                Ibin[i,j,t] = math.floor(I[i,j,t] * 255 / bin);

    weights,X,labels = im3Dhist(I,Ibin,bin);

    cinits = np.zeros([k,3]);
    cw = weights;
    N = X.shape[0]
    sigma2 = sigma  ** 2;

    for i in range(k):
        id = np.argmax(cw,axis = 0);

        cinits[i,:] = X[id,:];
        d2 = np.tile(cinits[i,:],(N,1)) - X;
        d2 = np.sum(d2*d2,axis=1);
        cw = np.array(cw);
        result_ = np.zeros(d2.shape);
        for j in range(len(d2)):
            result_[j] = 1 - math.exp(-d2[j]/sigma2);
        cw = cw * result_;

    [a,C,b] = fkmeans(X,cinits,weights);

    C = lab2rgb_matrix(C);
    C = np.transpose(C);
    C_new = [];
    k = 0;
    for i in range(C.shape[0]):
        CC = C[i,:];
        if CC.all() == 0:
            continue;
        else:
            k = k + 1;
            C_new.append(C[i,:]);

    C_new = np.array(C_new);

    return C_new , weights;



def im3Dhist(I, Ibin, bin):
    h,w,c = I.shape;
    h1,w1,c1 = Ibin.shape;
    Ibin = Ibin.reshape(h1*w1,c1,order="F");
    n = bin;
    J = Ibin[:,0]*n*n + Ibin[:,1]*n + Ibin[:,2] + 1 ;
    N = h*w;
    M = n*n*n;

    I = I * 255;
    lab_image_pixel = I.reshape(h * w, c, order="F");
    lab_image = rgb2lab_matrix(lab_image_pixel);
    lab_image_pixel = lab_image;


    weights = np.zeros([M,2]);
    csums = np.zeros([M,3]);
    for i in range(N):
        if J[i] < 0 or J[i] > M:
            continue;

        k = int(J[i]);
        weights[k,0] = weights[k,0] + 1;
        weights[k,1] = J[i];
        csums[k,:] = csums[k,:] + lab_image_pixel[i,:];

    ids = np.where(weights[:,0]!=0);
    ids = np.array(ids);
    ids = ids.T;
    W = weights[ids[:,0],:];
    C = csums[ids[:,0],:];


    AA = np.tile(W[:, 0],(3,1))
    AA = AA.T;
    C = C / AA;

    labels = np.zeros(Ibin.shape);
    label = np.zeros(Ibin.shape);
    for i in range(W.shape[0]):
        labels[J==W[i,1]]=i;
        for j in range(J.shape[0]):
            if J[j] == W[i,1]:
                label[j,0] = i;
    labels = labels.reshape([h,w,3]);
    W = W[:,0];

    return W,C,labels;
