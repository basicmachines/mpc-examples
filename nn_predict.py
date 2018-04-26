import mlpnet as mlp
import numpy as np

net = mlp.MLPNetwork(
    ndim=[6, 25, 1],
    act_funcs=['tanh', 'linear'],
    name='MIP 2',
    cost_function='mse'
)

weights_trained = np.array([
        4.09001604e+00,  3.65528500e+01, -2.01644144e+01, -3.20389191e+00,
        1.43024020e+01,  5.01238661e-01, -9.48105229e+00,  3.59863630e-02,
       -1.16098455e-01, -1.66856097e+00, -4.73227012e-01,  2.30698977e+00,
        4.56777190e-02,  4.25125574e-01, -1.82182640e+01, -8.43009621e+00,
       -1.63633145e+01, -2.99817030e+01, -1.52176931e+01, -3.06781925e+01,
        1.04873531e+01, -1.43639600e-02, -9.74897697e-01,  1.16276755e+00,
        4.44013317e-01,  2.03056438e+00,  6.20478742e-01, -1.22386970e-01,
       -1.52679982e+00,  3.20290120e-02,  8.14544166e-01,  1.07293576e+00,
        1.78329009e+00,  1.37705973e+00, -3.36937648e-01, -4.04538670e-02,
       -3.91797601e-01, -1.67361153e+01, -8.58026295e-01, -1.46627608e+01,
       -1.10195540e+00,  4.22428053e+00,  1.55192580e+01,  4.14833966e+00,
        3.43891422e+01, -2.25120014e+00,  3.83492774e+01, -9.68096086e-01,
       -5.79565885e+00,  4.56493761e+01, -1.36296014e+01, -1.77002809e+01,
       -1.55061365e+01, -2.33339298e+00, -1.79384336e+01, -1.96683372e+01,
        5.93503227e+00,  5.30872900e+01, -1.11340496e+01, -3.39674386e+00,
        3.49426939e+01,  1.13152124e+01, -8.16739111e+00, -2.69490902e+01,
        9.94362470e+00,  2.62512313e+00,  3.03234800e+01,  2.27560998e+00,
        1.74791063e+01, -1.14091618e-01,  8.85840353e+00,  1.83596219e+01,
        1.43300602e+01, -3.48107759e+00,  3.22159485e+01,  1.73750671e+00,
       -3.63895423e+00,  2.21489544e+00,  1.09343189e-01,  7.42068280e-01,
        1.34143163e+00,  1.96834004e+00,  1.73627550e+00, -2.76556839e-01,
        6.57080833e+00,  5.67703737e+01, -2.44826238e+01, -8.11811536e+00,
        2.65358708e+01,  5.44781391e+00, -5.77498413e+00, -1.62607680e-01,
       -1.72581792e-01, -6.54536807e+00,  6.83679562e-01, -1.17450341e+01,
       -2.07487968e-01,  1.61975318e+00,  2.15299508e-01, -4.82896439e-01,
       -6.91921000e-01, -9.19148060e-02, -6.97314666e-01, -1.09532644e-01,
        3.06502031e-01, -1.54752734e+00,  1.71750708e-01, -2.53028730e+00,
       -7.52225922e-01, -5.21045721e+00, -1.49624709e+00,  7.87217527e-01,
       -7.78387013e+00, -8.46859494e+00, -1.56277495e+01, -2.39067558e+01,
       -2.70848133e+01, -1.46425753e+01,  7.24930206e+00, -1.06800620e-02,
        1.84316258e-01, -6.95939340e+00, -1.24000881e+00, -6.19892300e+00,
       -1.53552679e+00,  1.69820512e+00,  5.40046500e-03, -8.29958802e-01,
        1.82357408e+01,  2.12793375e+00,  1.73192172e+01,  3.00323065e+00,
       -4.37705142e+00,  2.03811932e+00,  1.13670436e-01, -2.06213387e+00,
       -4.54884357e-01, -5.64723844e+00, -1.38041788e+00,  6.27791309e-01,
       -4.81138105e+00,  5.85765926e+01, -1.41020937e+01,  1.05015577e+00,
        4.02473649e+01, -1.36339382e+00, -4.26637646e+00, -2.79595572e+00,
        2.68719438e+01,  1.06339621e+01,  1.15512350e+01,  3.38991163e+01,
        1.25955031e+01, -6.43934842e+00, -3.84469101e+00,  3.33933527e+01,
       -6.01585703e+00, -4.04138549e+00,  1.82477633e+01,  2.73871035e+00,
       -2.52040067e+00, -1.84619970e-02, -3.56249485e-01,  1.27791516e+00,
        1.04288146e+00,  1.48400111e+00,  1.15161182e+00, -5.14959528e-01,
       -2.56693070e+00,  3.18224890e+01, -1.30026973e+01,  5.92237067e+00,
       -7.36787885e+00,  1.18567108e+01,  1.32207365e+00,  1.12262022e+01,
       -2.14544735e+00,  2.16747193e+02, -8.61190748e+00,  1.02051215e+02,
        1.34102271e+02, -1.62991509e+02,  1.72516791e+01, -5.98948348e+00,
        2.80121151e+01,  4.15492486e+00,  3.70490366e+00,  1.00566234e+02,
       -2.84291963e+01,  5.77048308e+01, -1.24051962e+02, -8.51799350e+01,
       -3.29105160e+00, -4.83022564e+02, -1.20682699e+02, -7.04117393e+01,
       -8.27455198e+00,  8.57657638e+00, -7.20731323e+00, -1.49304709e+02,
        4.17111805e+00
])

net.set_weights(weights_trained)

net.mu = np.array([
       0.16908481,  0.00710793,  0.00499091,
       -0.0007912, -0.00321155,  0.02138913
])

net.sigma = np.array([
     176.90106476,   0.46416354,   0.32408576,
       0.30715732,   0.27347225,   0.45905399
])

def next_tau(tau, θw, θw_dot, θr, θr_dot, xr_sp):

    x = tau, θw, θw_dot, θr, θr_dot, xr_sp

    tau_p1 = net.predict(x)[0,0]

    return tau_p1