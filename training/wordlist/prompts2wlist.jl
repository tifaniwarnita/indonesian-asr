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

function prompts2wlist(prompts, wlist)
  if ! isfile(prompts)
    error("can't find prompts file: $prompts")
  end

  wordhash = Dict{String, Int32}()
  prompts_fh=open(readlines, prompts)    
  for lineln=prompts_fh
    line=chomp(lineln)
    line_array=split(line,r"\s+"); 
    shift!(line_array)
    for word=line_array
      wordhash[word]=1
    end
  end
  wordhash["SENT-END"]=1
  wordhash["SENT-START"]=1

  wordlist = keys(wordhash) # returns an iterator
  wlist_arr=Array(String,length(wordhash))
  i=1
  for word=wordlist
    wlist_arr[i] = word * "\n"
    i=i+1
  end
  sortedwlist_arr=sort(wlist_arr)

  wlist_fh=open(wlist,"w"); 
  write(wlist_fh,sortedwlist_arr); 
  close(wlist_fh)  
end

# if called from command line
if length(ARGS) > 0 
  if ! isfile(ARGS[1])
    error("can't find prompts file: $ARGS[1]")
  end
  if length(ARGS) <= 2 
    prompts2wlist(ARGS[1],ARGS[2] )
  else
    error("prompts2list: too many arguments for call from command line")
  end
  
end


