#!/usr/bin/python3
import os,argparse,sys

#Parsing command line arguments (including a description and help file).
#parser = argparse.ArgumentParser(add_help=False,
        #description = "Script to recursively build a directory.")

#parser.add_argument("-h", "--help", action = "help", default=argparse.SUPPRESS, help = "Show options.")
#parser.add_argument("-p","--path", help = "Specify a custom path for your directory (Default is the current directory).",nargs="?",const=1,default=os.getcwd())
#parser.add_argument("-n", "--name", help = "Specify custom names for your folders (Default is \'new_folder\').",nargs="?",const=1,default="new_folder")
#parser.add_argument("-d","--depth", help = "Specify the depth of your directory structure (Default is 1).",nargs="?",type=int, const=1,default=1)
#args = parser.parse_args()

#if len(sys.argv[1:])==0:
    #parser.print_help()
    #exit(1)


#if (args.PATH,args.NAME,args.DEPTH):
    #dir_name,dir_path,dir_depth = args.PATH,args.NAME,args.PATH

#print(args.path)




def build_directory(name,path,depth):
    path = path + "/" + name
    i = 0
    while i <= depth:
        os.makedirs(path)
        path += "/" + name + str(i)
        i += 1
        continue



if __name__=='__main__':

#Parsing command line arguments (including a description and help file).
    parser = argparse.ArgumentParser(add_help=False,
        description = "Script to recursively build a directory.")

    parser.add_argument("-h", "--help", action = "help", default=argparse.SUPPRESS, help = "Show options.")
    parser.add_argument("-p","--path", help = "Specify a custom path for your directory (Default is the current directory).",nargs="?",const=1,default=os.getcwd())
    parser.add_argument("-n", "--name", help = "Specify custom names for your folders (Default is \'new_folder\').",nargs="?",const=1,default="new_folder")
    parser.add_argument("-d","--depth", help = "Specify the depth of your directory structure (Default is 2).",nargs="?",type=int, const=1,default=2)
    args = parser.parse_args()
    print(args)

    build_directory(args.name,args.path,args.depth)

