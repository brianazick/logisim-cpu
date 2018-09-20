#presuming all registers begin empty
# when this code is done running
# $4 should contain 4
# $5 should contain 5
# if $4 contains 1, then your first branch failed
# by being taken when it shouldn't be taken
# if $5 contains 7, then your second branch failed
# by not being taken when it should be taken

addi $1 $0 1
addi $2 $0 2
addi $3 $0 1
addi $4 $0 1
addi $5 $0 5
beq $1 $2 3  #you should not take this branch
addi $4 $4 1
addi $4 $4 1
addi $4 $4 1
beq $1 $3 2 # you should take this branch
addi $5 $5 1
addi $5 $5 1

