import sys
sys.path.insert(0, '../Models/')
import dill
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

from model_recursive_class import model_recursive
from Benchmark.model_class import model
from Benchmark.model_recursive_nnpde_class import model_recursive_nnpde

import os

if __name__ == '__main__':
    params={'rhoE': 0.05, 'rhoH': 0.05, 'aE': 0.15, 'aH': 0.03,
            'alpha':0.5, 'kappa':5, 'delta':0.05, 'zbar':0.1, 
            'lambda_d':0.03, 'sigma':0.06, 'gammaE':2, 'gammaH':2,'maxIterations':400}
    params['scale']=2
    model1 = model_recursive(params)
    #model1.maxIterations=15
    model1.solve()
    
    model2 = model_recursive_nnpde(params)
    model2.solve()

    plt.figure()
    plt.plot(model1.z[3:],model1.mu_z[3:], label = 'Finite Difference') 
    plt.plot(model2.z[3:], model2.mu_z[3:], label = 'Neural Network', linewidth=6, linestyle='dotted')
    plt.legend(loc=1,prop={'size': 15})
    plt.xlabel('Wealth share', fontsize=15)
    plt.ylabel('Drift of wealth share',fontsize=15)
    plt.savefig('../output/plots/nnpde_comparison_mu_z.png')
    
    
    plt.figure()
    plt.plot(model1.z[3:],model1.q[3:], label = 'Finite Difference') 
    plt.plot(model2.z[3:], model2.q[3:], label = 'Neural Network', linewidth=6, linestyle='dotted')
    plt.legend(loc=4,prop={'size': 15})
    plt.xlabel('Wealth share', fontsize=15)
    plt.ylabel('Capital price',fontsize=15)
    plt.savefig('../output/plots/nnpde_comparison_q.png')
    
    plt.figure()
    plt.plot(model1.z[3:],model1.ssq[3:], label = 'Finite Difference') 
    plt.plot(model2.z[3:], model2.ssq[3:], label = 'Neural Network', linewidth=6, linestyle='dotted')
    plt.legend(loc=1,prop={'size': 15})
    plt.xlabel('Wealth share', fontsize=15)
    plt.ylabel('Return volatility',fontsize=15)
    plt.ylim(0.05,0.25)
    plt.savefig('../output/plots/nnpde_comparison_ssq.png')
    
    plt.figure()
    plt.plot(model1.z[3:],model1.psi[3:], label = 'Finite Difference') 
    plt.plot(model2.z[3:], model2.psi[3:], label = 'Neural Network', linewidth=6, linestyle='dotted')
    plt.legend(loc=4,prop={'size': 15})
    plt.xlabel('Wealth share', fontsize=15)
    plt.ylabel('Capital share',fontsize=15)
    plt.ylim(0.1,1.1)
    plt.savefig('../output/plots/nnpde_comparison_psi.png')
    
    plt.figure()
    plt.plot(model2.amax_vec)
    plt.plot(model1.amax_vec[0:15])

