import sys

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................
"""

#zadanie slova pre spustenie programu
print("Zadaj slovo: ")
slovo = input('> ')

#ak je slovo prazdne ukonci ulohu
if slovo == '':
    sys.exit()

#loop ktory prechadza cez riadok po riadku a nahradza * znakmi slova
for line in bitmap.splitlines():
    #loop cez nahradzanie * v riadkoch
    for i, bit in enumerate(line):
        if bit == " ":
        #nahrad medzeru medzerou
            print(" ", end="")
        else:
            #vypis charakter slova
            print(slovo[i%len(slovo)], end="")
    print()

