from domainExample import Tians

# try commenting out (without this the namespace 'domain' is unavailable):
import domainExample

sebastian = Tians()
christian = domainExample.Tians()
tobi = domainExample.Tobiwan()
tobi_class = domainExample.Tobiwan

print(
    "So the only risk would actually be importing the same thing twice."
)

print(tobi)
print(tobi_class)
print(christian)
print(
    sebastian
)  # <- interestingly the namespace is still clear if you print the object
