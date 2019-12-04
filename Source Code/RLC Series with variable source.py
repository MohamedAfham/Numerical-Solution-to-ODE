import numpy as np
import matplotlib.pyplot as plt

R = 2 #Resistance
L = 1 #Inductance
C = 1 #Capacitance
Vm = 5 #Max.Source Voltage
T_f = 20 #Final Time
i_0 = 0 #Initial Current
i_dot_0 = 100 #Initial i_dot 
w = 1 #Omega

#Define a function which returns the second derivative of current

def i_double_dot(R,L,C,Vm,w,t,i,i_dot):
    return Vm*w*np.cos(w*t)/L +(-1)*((R*i_dot/L)+(i/(L*C)))

#Implement the Euler's method

def CurrentVec (T_f,nt):
    tvec = np.linspace(0,T_f,nt+1)      #Vector of the x_values of the graph
    ivec = np.zeros(tvec.size)          #Vector of the current at corresponding time
    i_dot_vec = np.zeros(tvec.size)
    ivec[0] = i_0
    i_dot_vec[0] = i_dot_0
    for j in range(1,tvec.size):        #For each time step looping to find the curent flow
        delta_t = tvec[j] - tvec[j-1]
        Current_double_dot = i_double_dot(R,L,C,Vm,w,tvec[j-1],ivec[j-1],i_dot_vec[j-1])
        i_dot_vec[j] = Current_double_dot*delta_t + i_dot_vec[j-1]
        ivec[j] = i_dot_vec[j]*delta_t + ivec[j-1]
    return [tvec,ivec]

iexact = CurrentVec(T_f,10000)  #Define the exact value as with very large time steps

iexact_nt50 = [iexact[0][0::200],iexact[1][0::200]]
iexact_nt100 = [iexact[0][0::100],iexact[1][0::100]]
iexact_nt500 = [iexact[0][0::20],iexact[1][0::20]]
iexact_nt1000 = [iexact[0][0::10],iexact[1][0::10]]

iEuler_nt50 = CurrentVec(T_f,50)
iEuler_nt100 = CurrentVec(T_f,100)
iEuler_nt500 = CurrentVec(T_f,500)
iEuler_nt1000 = CurrentVec(T_f,1000)

Err_nt50 = abs(iexact_nt50[1] - iEuler_nt50[1])
Err_nt100 = abs(iexact_nt100[1] - iEuler_nt100[1])
Err_nt500 = abs(iexact_nt500[1] - iEuler_nt500[1])
Err_nt1000 = abs(iexact_nt1000[1] - iEuler_nt1000[1])


dtVec = [iEuler_nt50[0][1]-iEuler_nt50[0][0],
         iEuler_nt100[0][1]-iEuler_nt100[0][0],
         iEuler_nt500[0][1]-iEuler_nt500[0][0],
         iEuler_nt1000[0][1]-iEuler_nt1000[0][0]]
ErrVec=[sum(Err_nt50)*(dtVec[0]),
        sum(Err_nt100)*(dtVec[1]),
        sum(Err_nt500)*(dtVec[2]),
        sum(Err_nt1000)*(dtVec[3])]

#################################################################################

fig, ax = plt.subplots()
ax.plot(iexact[0],iexact[1],'k--',label='Exact Solution')
ax.plot(iEuler_nt50[0],iEuler_nt50[1],'r',
         label='Numerical Solution with 50 time steps')
ax.plot(iEuler_nt100[0],iEuler_nt100[1],'g',
         label='Numerical Solution with 100 time steps')
ax.plot(iEuler_nt500[0],iEuler_nt500[1],'b',
         label='Numerical Solution with 500 time steps')
ax.plot(iEuler_nt1000[0],iEuler_nt1000[1],'m',
         label='Numerical Solution with 1000 time steps')  
legend = ax.legend(loc='upper center', shadow=True, fontsize='medium')

plt.xlabel('Time(s)')
plt.ylabel('Current Flow(A)')
plt.title('Current Flow vs Time')

#################################################################################

fig, ax = plt.subplots()
ax.plot(iEuler_nt50[0],Err_nt50,'r',label='Error plot with 50 time steps')
ax.plot(iEuler_nt100[0],Err_nt100,'g',label='Error plot with 100 time steps')
ax.plot(iEuler_nt500[0],Err_nt500,'b',label='Error plot with 500 time steps')
ax.plot(iEuler_nt1000[0],Err_nt1000,'m',label='Error plot with 1000 time steps')
plt.xlabel('Time(s)')
plt.ylabel('|Exact Current - Numerical Current|(A)')
plt.title('Error vs Time')
legend = ax.legend(loc='upper center', shadow=True, fontsize='medium')

#################################################################################

fig, ax = plt.subplots()
ax.plot(dtVec,ErrVec,'k-x',label='Integral Error vs Size of time-step')
plt.xlabel('Size of time-step(dt)')
plt.ylabel('Integral of error in current solution over time')
plt.title('Integral Error vs Size of time-step')
plt.show()

#################################################################################
    
