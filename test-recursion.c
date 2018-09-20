//this is pseudo-code, obviously.
//you'll need to compile this down to your own assembly.


int RecurAdd(int a, int b) {

if (a == 0)
	return b
else 
	return 1 + RecurAdd(a-1, b)

}

int RecurMul(int a, int b){

if (a == 1)
	return b
else
	return b + RecurMul(a-1,b)

}
