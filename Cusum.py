#!/usr/bin/python

import math
import utils
import matplotlib.pyplot as plt

######################################################
#This is really only effective as a one-sided cusum.
#The other side (the low side) seems to be... odd.
def cusum(vals, k, h):
   """
   """
   shvals = []
   slvals = []
   hlist = []
   nhlist = []
   npos = 0
   nneg = 0
   sh = 0
   sl = 0
   for val in vals: 
      hlist.append(h)
      nhlist.append(-h)
      sh += max(0, val - k + sh)
      sl += min(0, val - k + sl)
      shvals.append(sh)
      slvals.append(sl)
      if sh >= h or sl <= -h:
         #print "Alarm"
         sh = 0 
         sl = 0
      #print "Curr. val: %.2f -- Curr. Sum High: %.2f -- Curr. Sum Low: %.2f" % (val, sh, sl)

   return (shvals, slvals, hlist, nhlist)



def esth(vals):
   """
   A reasonable estimate for h is approx. 5 * sigma.
   (i.e. 5 * std. deviation of samples.)
   """
   return 5.0 * utils.stddev(vals)
   

def buildk(vals, ma, s=1.5):
   """
   According to Kemp (1962), the expression for determing a target value
   k for cusum should be done via:

         k = mean_a + .5 delta
         (Where: delta is the mean shift we want to detect.
                 mean_a is an "acceptable process mean value."
                 mean_a is the mean of the original dataset.) 

   Lucas et al. (1982) suggested it be close to .5 delta as well,
   and it should be chosen close to:

                    mean_d - mean_a
         k = ---------------------------
               ln (mean_d) - ln (mean_a)

   Mean_d is the "barely tolerable mean value".  This is the mean that
   CUSUM should quickly detect.  Mean_d is based on the declared needs
   of an experimental designer, the mean, and the std dev.

      mean_d = s * p + mean_a 
      (Where: s is a value chosen by the experimental designers,
              p is the standard deviation, and mean_a is the mean
              of the dataset.)
   """
   md = s * utils.stddev(vals) + ma
   return (md - ma) / (math.log(md, math.e) - math.log(ma, math.e))
   
   

if __name__ == "__main__":

   #Diabetic disease data
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

   k = buildk(ddd, utils.mean(ddd))
   shvals, slvals, hlist, nhlist = cusum(ddd, k, 14) 

   plt.plot([0,1,3,0,2,4,8,6,4,0], "-go")
   plt.plot(shvals, "-go")
   plt.plot(slvals, "-bo")
   plt.plot(hlist, "-rx")
   plt.plot(nhlist, "-rx")

   plt.show() 
















