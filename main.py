import third
import second
from second import say_hey

import package
import package.names, package.greetings

from random import randint, choice


'''

'''

second.say_hey()

third.shoutout_from_third()
print(third.name)

print(package.NAME)

package.greetings.greeting(package.names.name1)
package.greetings.greeting(package.names.name2)

print(randint(1, 10))

a = (1,2,3,4)
print(choice(a))

print(a)

(q,w,e,r) = a
print(q)

print "HOHO"