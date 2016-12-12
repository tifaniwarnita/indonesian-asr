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

function prompts2mlf(prompts, mlf) 
  mlf=open(mlf,"w"); 

  write(mlf,"\#\!MLF\!\#\n")
  prompts_arr=open(readlines, prompts)    
  for lineln=prompts_arr
    line=chomp(lineln)
    line_array=split(line,r"\s+"); 
    fname=shift!(line_array)
    write(mlf,"\"$fname.lab\"\n")
    for word=line_array
        write(mlf,"$word\n")
    end
    write(mlf,".\n")
  end

  close(mlf)
end

# if called from command line
if length(ARGS) > 0 
  if ! isfile(ARGS[1])
    error("can't find prompts file: $ARGS[1]")
  end
  if length(ARGS) <= 2 
    prompts2mlf(ARGS[1],ARGS[2] )
  else
    error("prompts2list: too many arguments for call from command line")
  end
  
end


