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

% set grid
[X,Y]=meshgrid(-0.5:size);
figure; hold on;
plot(X,Y,'k');
plot(Y,X,'k');
axis off;

plot(A(:, 1), A(:, 2), 'r-', 'clipping', 'off', LineWidth=2); 

offset = 0.4;
% add cell numbers to the grid
for i = 0:length(A)-1
    x_pos = A(i+1, 1); % X-coordinate of the end point of the line segment
    y_pos = A(i+1, 2); % Y-coordinate of the end point of the line segment
    cell_number = i;
    text(x_pos - offset, y_pos - offset, num2str(cell_number), 'HorizontalAlignment', 'left', 'VerticalAlignment', 'bottom', 'FontSize', 9);
end

axis equal, axis off
