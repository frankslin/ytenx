# coding=utf-8
from django.http import Http404
from django.shortcuts import render
from django.core.paginator import InvalidPage, EmptyPage
from ytenx.helpers.paginator import Paginator

def byoh_lyuk(request, name):
  if name == 'KienxPyan':
    return kienx_pyan(request)

  if not name:
    name = 'miuk_lyuk'
  
  path = 'byohlyuk/' + name + '.html'
  # Pages that reference files only available via Worker Static Assets, not the CDN.
  local_static = {'IPA_Charts'}
  context = {'STATIC_URL': '/static/'} if name in local_static else {}
  try:
    return render(request, path, context)
  except:
    raise Http404()

def kienx_pyan(request):
  import os
  pwd = os.path.dirname(__file__)

  kienx_pyan_pieux = []
  for line in open(pwd + '/st_multi.txt'):
    line = line[:-1]
    line = line.split('\t')
    kienx_pyan_pieux.append(line)

  return render(request, 'byohlyuk/KienxPyan.html', {
    'kienx_pyan_pieux': kienx_pyan_pieux,
  })
