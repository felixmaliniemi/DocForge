% Detta är ett exempel på addition
function result = add(a,b)
    % Returnerar summan av a och b
    result = a + b;
end

function result = subtract(a,b)
    % Returnerar skillnaden mellan a och b
    result = a - b;
end

function result = multiply(a,b)
    % Returnerar produkten av a och b
    result = a * b;
end

function result = divide(a,b)
    % Returnerar kvoten av a och b
    if b == 0
        result = NaN;
    else
        result = a / b;
    end
end

% Main script
disp(['Addition: ', num2str(add(3,2))]);
disp(['Subtraction: ', num2str(subtract(5,3))]);
disp(['Multiplication: ', num2str(multiply(4,2))]);
disp(['Division: ', num2str(divide(10,2))]);
