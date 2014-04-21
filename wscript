#!/usr/bin/env python
'''
Copy this file locally and modify DOCMAIN
'''

DOCMAIN = "test-beamer"

top = "."
out = "output"


import os

def options(opt):
    opt.load('tex')

def configure(cfg):
    cfg.load('tex')
    cfg.env.append_value('PDFLATEXFLAGS','-halt-on-error')
    cfg.env.TEXINPUTS = os.path.expandvars("$HOME/git/bvtex")

def build(bld):
    for main in DOCMAIN.split():
        bld(features = 'tex',
            type = 'pdflatex',
            source = main+'.tex',
            outs = 'pdf',
            prompt = 0)
