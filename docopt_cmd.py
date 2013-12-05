

def _argnames(func):
    return func.func_code.co_varnames[:func.func_code.co_argcount]


class cmd(object):
    _specdict = {}

    def __init__(self, cmdspec, **argspec):
        if callable(cmdspec):
            #don't break original function
            self.__call__ = self.func = cmdspec
            self.cmdspec = tuple(cmdspec.__name__.split('_'))
            self.argspec = {}
            for arg in _argnames(self.func):
                self.argspec[arg] = '--'+arg
            cmd._register(self)
        else:
            self.cmdspec = tuple(cmdspec.split())
            self.argspec = argspec

    def __call__(self, func):
        self.func = func
        cmd._register(self)
        return func

    @classmethod
    def _register(cls, inst):
        cls._specdict[inst.cmdspec] = inst.argspec, inst.func

    @classmethod
    def dispatch(cls, args):
        #sort by num of subcommands, to prevent false matches
        s = sorted(cls._specdict.items(), key=lambda x: len(x[0]), reverse=True)
        for cmd_spec, fspec in s:
            if all(args[cmd] for cmd in cmd_spec):
                arg_spec, func = fspec
                for name, mapping in arg_spec.items():
                    arg_spec[name] = args[mapping]
                func(**arg_spec)
