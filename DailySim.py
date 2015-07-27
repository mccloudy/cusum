#!/usr/bin/python

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline,interp1d

import utils

def euc_day_sim(d1, d2):
   """
   Euclidian daily similarity for two sequences of identical lengths.
   """
   if len(d1) != len(d2): return None

   d = 0.0
   n = len(d1)
   for i in range(0, len(d1)):
      for j in range(i+1, len(d2)):
         d += abs(d1[i] - d2[j]) / ((n-1.0) * ((n-2.0)) / 2.0)
         
   return d



def dtwd(s, t): #s from 1..n, t from 1..m
   """
   Dynamic Time Warping for two sequences of identical lengths.
   (Taken from wikipedia)
   """
   n = len(s)
   m = len(t)
   dtwm = np.zeros((n, m)) #n+1 x m+1 matrix

   for i in range(1, n):
      dtwm[i][0] = float("inf")
   for i in range(1, m):
      dtwm[0][i] = float("inf")
   dtwm[0][0] = 0

   for i in range(0, n):
      for j in range(0, m):
         cost = abs(s[i] - t[j])
         dtwm[i][j] = cost + min(dtwm[i-1][j],   # insertion
                                 dtwm[i][j-1],   # deletion
                                 dtwm[i-1][j-1]) # match

   return dtwm[n-1][m-1]

 

if __name__ == "__main__":
   
   ddd = [20, 23, 16, 19, 23, 16, 22, 12, 9, 17, 20, 18, #1974
         2, 8, 8, 23, 14, 25, 16, 25, 7, 2, 3, 13, #1975
         20, 18, 30, 17, 23, 21, 14, 22, 18, 18, 13, 27, #1976
         25, 20, 31, 22, 15, 26, 21, 23, 14, 13, 58, 15, #1977
         29, 27, 25, 10, 17, 17, 30, 22, 14, 15, 14, 14,
         24, 14, 19, 9, 11, 7, 19, 8, 19, 22, 11, 22,
         25, 22, 19, 23, 17, 17, 10 ,23, 24, 15, 41, 16,
         15, 7, 10, 26, 9, 17, 23, 22, 30, 32, 22, 27,
         25, 20, 35, 17, 19, 19, 27, 29, 11, 23, 25, 16,
         24, 20, 19, 12, 16, 10, 9, 16, 7, 9, 18, 9,
         18, 17, 14, 14, 19, 23, 12, 20, 7, 17, 9, 14,
         18, 2, 6, 18, 14, 17, 22, 12, 18, 13, 6, 18,  #1985
         21, 17] #1986
   
   d1 = [20, 23, 16, 19, 23, 16, 22, 12, 9, 17, 20, 18, #1974
      2, 8, 8, 23, 14, 25, 16, 25, 7, 2, 3, 13, #1975
      20, 18, 30, 17, 23, 21, 14, 22, 18, 18, 13, 27, #1976
      25, 20, 31, 22, 15, 26, 21, 23, 14, 13, 58, 15, #1977
      29, 27, 25, 10, 17, 17, 30, 22, 14, 15, 14, 14,
      24, 14, 19, 9, 11, 7, 19, 8, 19, 22, 11, 22]
   
   d2 = [10, 6, 7, 14, 14, 5, 5, 1, 2, 3, 4, 10, 
      14, 18, 19, 20, 13, 14, 10, 10, 5, 4, 6, 16,
      20, 23, 16, 19, 23, 16, 22, 12, 9, 17, 20, 18, #1974
      2, 8, 8, 23, 14, 25, 16, 25, 7, 2, 3, 13, #1975
      20, 18, 30, 17, 23, 21, 14, 22, 18, 18, 13, 27, #1976
      25, 20, 31, 22, 15, 26, 21, 23, 14, 13, 58, 15] #1977
         

   #print euc_day_sim(ddd)
   d1 = utils.norm_by_max(d1)
   d2 = utils.norm_by_max(d2)
   print euc_day_sim(d1, d2)
   print dtwd(d1, d2)

   plt.plot(d1, "-rx")
   plt.plot(d2, "-go")
   plt.show()

