def heron(square, sqrtGuess, tol=1e-3):
    import matplotlib.pyplot as plt
    x = []; error = []
    x.append(sqrtGuess); S = square
    error = tol + 1 #Arbitrary default value
    k = 0
    while abs(error) >= tol:
        x.append((x[k] + (S/x[k])) * 0.5)
        error = abs(x[k+1]) - abs(x[k])
        k = k + 1
    plt.plot(list(range(1,k+2)),x,'r--')
    plt.plot(list(range(1,k+2)),x,'go')
    plt.xlabel('Iteration'); plt.ylabel('Square Root'); plt.title('Convergence Plot'); plt.grid(True)
