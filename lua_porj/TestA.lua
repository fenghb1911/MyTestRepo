print("-----------Another file for Test start--------")

--f = load("local a = 10; return a + 20")

--print(f()) --> 30
--io.write(f() .. "\n")

a = 'alo\n123"'
--print(a)

a = "alo\n123\""
--print(a)

a = '\97lo\10\04923"'
--print(a)

a = [[alo
123"]]
--print(a)

a = [==[
alo
123"]==]
--print(a)

a = [[
<HTML>
<HEAD>
<TITLE>An HTML Page</TITLE>
</HEAD>
<BODY>
Lua
[[a text between double brackets
</BODY>
</HTML>
]]
--print(a)

for i=10,1,-1 do
   print(i)
end

print("-----------Another file for Test end----------")