clc;
clear;
close all;

%% plot the objective function

% define the function as anonymous function handle
% you can then evaluate it as f(x,y) (elementwise)
f = @(x,y) .5*( (x-1).^2 + 100*(y-x.^2).^2 + y.^2);

% Create circle grid of x y values 
R=0:.002:sqrt(2);
TH=2*pi*(0:.002:1); 
X=R'*cos(TH); 
Y=R'*sin(TH);
% calculate objective function values
% add 1 and take log for better visualization
Z=log( 1 + f(X,Y));

figure(1); clf;
colormap('gray');

% subplot 1 with surface plot and contour plot
subplot(1,2,1); hold on
view([124 34]);
grid('on'); axis square;
surf(X,Y,Z,'LineStyle','none');
contour(X,Y,Z);
title('Surface and contour plot of the nonlinear function');
xlabel('x')
ylabel('y')
zlabel('log(1+f(x,y))')

% subplot 2 with contour plot only
subplot(1,2,2); hold on
grid('on'); axis square;
contour(X,Y,Z, 'Displayname', '$f(x,y)$');
% read current axis limits and fix them at these values
ax = axis(); axis(ax);


%% grad and hessians

% gradient
fgrad = @(x,y) [x-1-200*x.*y+200*x.^3;
                101*y - 100* x.^2 ];

% true hessian
fhess = @(x,y) [1-200*y+600*x^2, -200*x;
                -200*x, 101];

% Gauss newton hessian
B_GN = @(x,y) [1+400*x^2, -200*x;
               -200*x   , 101];
            
z0 = [-1;-1];                            % initial guesss
tol = 1e-3;                             % tolerance for stopping criterion
maxit = 5000;
%% newton Type algorithms
% introduce z = [x;y]
fgradz = @(z) fgrad(z(1), z(2));
% exact hessian
tic
[Z_ex, grad_ex] = newtonType(fgradz, @(z) fhess(z(1), z(2)), z0, tol, maxit);
t_ex = toc;
% Gauss Newton
tic
[Z_GN, grad_GN] = newtonType(fgradz, @(z) B_GN(z(1), z(2)), z0, tol, maxit);
t_GN = toc;

%% print infos
fprintf('\n-----------------------------------\n')
fprintf('Method\t\t  #iter\t  t in s\n')
fprintf('-----------------------------------\n')
fprintf('exact hessian      %4d   %.3e\n', size(Z_ex,2)-1, t_ex)
fprintf('Gauss-Newton       %4d   %.3e\n', size(Z_GN,2)-1, t_GN)

%% add iterates to plot
figure(1); subplot(1,2,2);
x = linspace(ax(1),ax(2),100);
plot(x, x.^2,'k--', 'Displayname', '$x=y^2$')
plot(Z_ex(1,:), Z_ex(2,:), 'b-x', 'Displayname', 'exact Hessian')
plot(Z_GN(1,:), Z_GN(2,:), 'r-x', 'Displayname', 'GN')
leg = legend('location', 'southeast');
set(leg,'interpreter','latex')

%% gauss newton error (3c)
N_GN = size(Z_GN, 2);           % number of GaussNewton iterations + 1
E_GN = zeros(N_GN, 1);          % Gauss-Newton error
for k = 1:N_GN
    fhess_k = fhess(Z_GN(1,k), Z_GN(2,k));  % evaluation exact hessian
    B_GN_k = B_GN(Z_GN(1,k), Z_GN(2,k));    % evaluation GN hessian
    E_GN(k) = norm(fhess_k - B_GN_k);      % norm of difference
end

figure(2);
plot(0:N_GN-1, E_GN)
title('Gauss-Newton Hessian approximation error')
xlabel('iteration k')
ylabel('frobenius norm of error')
