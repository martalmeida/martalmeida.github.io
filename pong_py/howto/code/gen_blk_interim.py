from okean.roms.inputs import surface

def gen_blk(year):
  path  = 'interim_data/%d' % year
  grid  = 'roms_grid.nc'
  fname = 'bulk_interim_%d.nc' % year

  args={}
  args['attr']   = {'dataset':'ECMWF ERA-Interim'} # add global atts
  args['model']  = 'roms' # or agrif
  args['tunits'] = 'days since 1970-01-01'
  args['keepor'] = False # also save data at original resolution in file

  surface.make_blk_interim(path,grid,fname,**args)


if __name__=='__main__':
  import sys
  y=int(sys.argv[1])
  gen_blk(y)
