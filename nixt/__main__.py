# This file is placed in the Public Domain.
#
# pylint: disable=C0103,C0413,W0105,W0212,


"""NIXT - you have been nixt.

    nixt  <cmd> [key=val] [key==val]
    nixt  [-a] [-c] [-h] [-v]

    options are:

    -a     load all modules
    -c     start console
    -h     show help
    -v     use verbose

    the cmd command show available commands.
    
    $ nixt cmd
    cfg,cmd,dpl,err,exp,imp,mod,mre,nme,pwd,rem,res,rss,thr

"""


from nixt.run.main import wrapped


if __name__ == "__main__":
    wrapped()
