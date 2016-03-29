
import numpy as np
from scipy.special import gamma, erfc
import sys
from subprocess import call

input_file_template = 'my_inputs.template'
input_file = 'my_inputs.txt'


print 'hi from test_driver'
print sys.argv

# Run dprepro to get right value into the file my_inputs.txt
call(['dprepro', sys.argv[1], input_file_template, input_file])

# Read the input file
f = open(input_file, 'r')
val = float( f.read() )
print 'read from file:', val

# Run the model

#Tsol = (Qm/k).*z + Ts_bar + D*(2^n)*gamma(((0.5*n)+1))*erfc(z./(sqrt(4*(k/(rho*cp))*t_star)));

n=0
yrs_warm=60
tstar=3600*24*365*yrs_warm
Ts_bar=-7.1
Qm=0.045
k=2.29
rho=2700
cp=926

z = [27.73685,42.97689,58.21692,73.45695,88.69698,103.937,119.177,134.4171,149.6571,164.8971,180.1372,195.3772,210.6172,225.8573,241.0973,256.3373,271.5773,286.8174,302.0574,317.2974,332.5375,347.7775,363.0175] 
T =[-5.32,-5.32,-5.29,-5.24,-5.11,-4.93,-4.67,-4.44,-4.14,-3.84,-3.56,-3.24,-2.95,-2.62,-2.35,-2.04,-1.78,-1.48,-1.18,-0.91,-0.6,-0.28,7.00E-02]

Tsol = (Qm/k)*z+Ts_bar+val*(2**n)*gamma(((0.5*n)+1))*erfc(z/(np.sqrt(4*(k/(rho*cp))*tstar)))

myfile = open(sys.argv[2], 'w')
myfile.write( str(np.sum((Tsol-T)**2)) )


