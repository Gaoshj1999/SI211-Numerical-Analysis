function [Z, F_res] = newtonType(F, B, z0, tol, maxit)
% Implentation of the newtonType method for finding the root of function F,
% i.e. a z for which ||F(z)|| <= tol \approx 0
% inputs:
%   F       vector valued function with identical number of input and
%           output arguments, F: R^n -> R^n
%           e.g. the gradient of a function
%   B       function handle of approximation of jacobian of F
%           e.g. the hessian approximation
%   z0      initial guess
%   tol     tolerance. Values smaller than this are considered 0
%   maxit   maximum number of iterations
%
% outputs:
%     Z     iteration history of input variable z
%     F_res iteration history of residual of F

    Z = z0;                                  % array to save history of z
    z = z0;                                  % initialize
    F_res = [];
    for i = 1:maxit
        F_eval = F(z);              % evaluate at current iterate
        F_res = [F_res, F_eval];    % save
        if norm(F_eval) <= tol      % check convergence criterion
            break
        end
        z = z - B(z) \ F_eval;        % newton type step
        Z = [Z,z];                  % save iterate
    end
    if i == maxit
        disp('maximum iterations reached')
    end
end
