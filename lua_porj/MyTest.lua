--print("Hello World")

dofile("TestA.lua")

function fact( n )
	-- body
	if n == 0 then
		return 1
	else
		return n * fact(n - 1)
	end
end
--[[
print("Enter a number:")
a = io.read("*number")
print(fact(a))]]

print(type(true))
print(type("1111"))
print(type(type))
print(type(fact))
print(type(123))