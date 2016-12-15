###############################################################################
#
#    Copyright (C) 2015  VoxForge
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

function fixfulllist(in_fulllist, in_monophones0, out_fulllist)
  seen=Dict{String, Int32}()
  in_fulllist_arr=open(readlines, in_fulllist) # automatically closes file handle
  in_monophones0_arr=open(readlines, in_monophones0) # automatically closes file handle
  new_fulllist_arr=cat(1,in_fulllist_arr, in_monophones0_arr)

  out_fulllist_fh=open(out_fulllist,"w")

  for phoneln=new_fulllist_arr
    phone=chomp(phoneln)
    if ! haskey(seen,phone) # remove duplicate monophone/triphone names
      seen[phone]=1
      write(out_fulllist_fh,phone * "\n")
    end
  end

  close(out_fulllist_fh)
end

# if called from command line
if length(ARGS) > 0 
  if ! isfile(ARGS[1])
    error("can't find fulllist file: $ARGS[1]")
  end
  if ! isfile(ARGS[2])
    error("can't find monophones0 file: $ARGS[2]")
  end
  if length(ARGS) > 3
    error("fixfulllist: too many arguments for call from command line\nusage: in_fulllist, in_monophones0, out_fulllist")
  end

  fixfulllist(ARGS[1], ARGS[2], ARGS[3])
end


