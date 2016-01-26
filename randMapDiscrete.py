import randPosDiscrete
def randMapDiscrete(Nx, Ny, Ngal, nanmask=1.):
    ''' 
    Make a map with randomly distributed galaxies.
    '''
    im = np.zeros((Nx,Ny))
    randx, randy = randPosDiscrete(Nx, Ny, Ngal)
    im[randx, randy] = 1.0
    im *= nanmask
    return im
