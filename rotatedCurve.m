% 4 empty matrices with 0 rows and 2 columns
A = zeros(0,2);
B = zeros(0,2);
C = zeros(0,2);
D = zeros(0,2);



% up and down is positive and negative along y-axis
% left and right are positive and negative along y axis
up = [ 0  1];
right  = [ 1  0];
down = [ 0 -1];
left  = [-1  0];

% set order and grid size
order = 2;
size = 2^(order);

% loop draws the curve by dividing the square into smaller squares and
% building the curve in each sub-square
for n = 1:order
  % temporary matrices
  AA = [B ; up ; A ; right  ; A ; down ; C];
  BB = [A ; right  ; B ; up ; B ; left  ; D];
  CC = [D ; left  ; C ; down ; C ; right  ; A];
  DD = [C ; down ; D ; left  ; D ; up ; B];
  
  A = AA;
  B = BB;
  C = CC;
  D = DD;
end

A = [0 0; cumsum(A)];

rotation_matrix = [0 1; -1 0];
A_rotated = A * rotation_matrix;
% 180 deg
% A_rotated = A_rotated * rotation_matrix; 
% 270 deg
% A_rotated = A_rotated * rotation_matrix;

% Create grid points
grid_points = linspace(1, 1, size+1);

% Plot the grid
figure; hold on;
for i = 1:size+1
    plot([grid_points(i) grid_points(i)], [grid_points(1) grid_points(end)], 'k'); % Vertical lines
    plot([grid_points(1) grid_points(end)], [grid_points(i) grid_points(i)], 'k'); % Horizontal lines
end
plot(A_rotated(:, 1), A_rotated(:, 2), '-or', 'clipping', 'off', 'LineWidth', 2);


axis equal, axis off
