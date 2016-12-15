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


function mktrihed(monophones, triphones, mktri) 
  monophones_arr=open(readlines, monophones)  # automatically closes file handle

  hed=open(mktri, "w") 
  write(hed, "CL $triphones\n")
  for phoneln=monophones_arr
    phone=chomp(phoneln)
    if length(phone)>0
      write(hed,"TI T_$phone {(*-$phone+*,$phone+*,*-$phone).transP}\n")
    end
  end
  close(hed)
end

# if called from command line
if length(ARGS) > 0 
  if ! isfile(ARGS[1])
    error("can't find monophones file: $ARGS[1]")
  end
  if ! isfile(ARGS[2])
    error("can't find triphones file: $ARGS[2]")
  end
  if length(ARGS) > 3 
    error("prompts2list: too many arguments for call from command line")
  end

  mktrihed(ARGS[1], ARGS[2], ARGS[3])
end


