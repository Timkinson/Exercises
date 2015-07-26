# -*- coding: utf-8 -*-
'''
Created on Jul 24, 2015

@author: Tim 
'''
import re

'''Given: string. Find palindrome'''

def check_palindrome(palind_candidate):
    
    is_palind = True
           
    for i in range(0, len(palind_candidate)//2):
        if palind_candidate[i] != palind_candidate[len(palind_candidate)-(i+1)]:
            is_palind = False
     
    return is_palind     
    
def main():

    st = "Rise to vote, sir"
        
    s = ''.join(re.findall("[a-zA-Z]+", st))
    s = s.lower()
        
    print("Original string: ", st)
    print("Simplified string: ", s)
    
    for j in range (3, len(s)):
        for i in range (0, len(s)):
            if (i + j - 1) == len(s):
                break
            palind_candidate = s[i:i+j]
            print('Is this palindrome? ', palind_candidate, ' The answer is ', check_palindrome(palind_candidate))
            
    print('Is whole string palindrome? "', s, '" The answer is ', check_palindrome(s))

if __name__ == '__main__':
    main()
        
'''
Able was I ere I saw Elba.
A man, a plan, a canal: Panama.
Doc, note, I Dissent. A fast never prevents a fatness. I diet on cod.
Dennis, Nell, Edna, Leon, Nedra, Anita, Rolf, Nora, Alice, Carol, Leo, Jane, Reed, Dena, Dale, Basil, Rae, Penny, Lana, Dave, Denny, Lena, Ida, Bernadette, Ben, Ray, Lila, Nina, Jo, Ira, Mara, Sara, Mario, Jan, Ina, Lily, Arne, Bette, Dan, Reba, Diane, Lynn, Ed, Eva, Dana, Lynne, Pearl, Isabel, Ada, Ned, Dee, Rena, Joel, Lora, Cecil, Aaron, Flora, Tina, Arden, Noel, and Ellen sinned.
I made border bard’s drowsy swords; drab, red robed am I.
Name no side in Eden, I’m mad! A maid I am, Adam mine; denied is one man.
Madam, I’m Adam.
Rats live on no evil star.
POW, ami! O’ Gad, ami! Go hang a salami, doc! Note; I dissent. A fast never prevents a fatness. I diet on cod. I’m a lasagna hog. I’m a dago! I’m a wop!
Nurse, I spy gypsies run.
Lion oil.
Dog's god.
Degas, are we not drawn onward, no? In union, drawn onward to new eras aged?
God’s dog.
Live evil.
Rise to vote, sir.
Too hot to hoot.
Dennis and Edna sinned.
Was it a cat I saw?
Was it a car or a cat I saw?
Evil olive
Dammit I'm mad
Racecar
Taco cat
Satan oscillate my metallic sonatas
Step on no Pets
A butt tuba
On a clover, if alive, erupts a vast pure evil; a fire volcano
Ten animals I slam in a net
Sit on a potato pan, Otis.
'''