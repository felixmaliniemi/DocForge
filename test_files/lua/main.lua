--[[
    MathOps.lua
    En modul med grundläggande matematiska operationer
]]

--[[
    Returnerar summan av två tal
]]
function add(a, b)
    return a + b
end

--[[
    Returnerar differensen av två tal
]]
function subtract(a, b)
    return a - b
end

--[[
    Returnerar produkten av två tal
]]
function multiply(a, b)
    return a * b
end

--[[
    Returnerar kvoten av två tal
]]
function divide(a, b)
    if b ~= 0 then return a / b else return nil end
end

--[[
    Startpunkt för programmet
]]
print("Addition: "..add(3,2))
print("Subtraction: "..subtract(5,3))
print("Multiplication: "..multiply(4,2))
print("Division: "..divide(10,2))
