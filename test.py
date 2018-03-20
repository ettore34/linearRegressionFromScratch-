from statistics import mean
import numpy as np 
#graph 
import matplotlib.pyplot as plt 
from matplotlib import style 

style .use('fivethirtyeight')

xs =np.array([1,2,3,4,5,6], dtype = np.float64)
ys = np.array([4,3,7,1,11,4] , dtype = np.float64)

#m slope and b = y 
# y = m*xmean + ymean
def best_fit_slope_and_intercept(xs,ys):
    m =( ((mean(xs)*mean(ys)) - (mean(xs*ys)))/
            ((mean(xs)*(mean(xs))) - (mean(xs*xs))   )) 

    b = mean(ys) - (m*mean(xs))
    return m,b

m,b = best_fit_slope_and_intercept(xs, ys)    

regression_line = [ (m*x) + b for x in xs ]

# with the best fit line we can make predictions 
# predicting on position 
x_predict = 9  
y_predict = m*x_predict + b
#plot prediction 
plt.scatter(x_predict ,y_predict , color = 'r')

plt.scatter(xs, ys)
plt.plot(xs, regression_line)
plt.show()