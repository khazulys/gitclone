from github import Github
import os


ACCESS_TOKEN = "ecba3d53a7e01851b648507ae04cd0e91e0ac427"
g = Github(ACCESS_TOKEN)

	#search
def main(keywords):
	query = '+'.join(keywords) + '+in:readme+in:description'
	result = g.search_repositories(query, 'stars', 'desc')
	print (f'\033[1;92m[√]\033[1;97m Found {result.totalCount} repo(s)\n')
	for repo in result:
		print (repo.clone_url)

def logo():
	print ("""

  \033[1;91m   ___ _ _   __                     _     
  \033[1;91m  / _ (_) |_/ _\ ___  __ _ _ __ ___| |__  
  \033[1;97m / /_\/ | __\ \ / _ \/ _` | '__/ __| '_ \ 
  \033[1;91m// /_\\| | |__\ \  __/ (_| | | | (__| | | |
  \033[1;91m\____/|_|\__\__/\___|\__,_|_|  \___|_| |_|

	      \033[1;96mGithub search in CLI
	        \033[1;97mCoded by khazul\n""")
                                          



if __name__ == '__main__':
	import os
	stop=False
	try:
		while(not stop):
			os.system('clear')
			logo()
			keywords = str(input('\033[1;92m[√]\033[1;97m Enter keyword: '))

			keywords = [keyword.strip() for keyword in keywords.split(',')]
			main(keywords)

			clone = str(input("\n\033[1;92m[√]\033[1;97m Git clone : "))

			def git():
				os.system('git clone {} &> /dev/null'.format(clone))

			from threading import Thread as khaz
			k = khaz(target=git)
			k.start()
			while k.is_alive():
				for i in "-\|/-\|/":
					import time
					print ("\r\033[1;92m[!]\033[1;97m Sedang mengcloning \033[1;92m"+i+'',end="",flush=True)
					time.sleep(0.1)
			print ("\n\033[1;92m[√]\033[1;97mDone")

			nanya = str(input("\n\033[1;92m[?]\033[1;97m Cari lagi? (y/t) "))
			if(nanya=="t"):
				stop=True

	except:
		pass
