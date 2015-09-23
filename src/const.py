'''
  Copyright (C) 2015 Eric Zhang, China
 
  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU Lesser General Public License as
  published by the Free Software Foundation, either version 3 of
  the License, or (at your option) any later version.
 
  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU Lesser General Public License for more details.
 
  You should have received a copy of the GNU Lesser General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
  Created on 2015-9-21
  @author: eric.zhang
  @contact: zgzczzw@163.com
  
'''
class const: 
    class ConstError(TypeError):pass 
    def __setattr__(self, name, value): 
        if self.__dict__.has_key(name): 
            raise self.ConstError, "Can't rebind const (%s)" % name 
        self.__dict__[name] = value
    MAX_LEN_PW = 16
    MIN_LEN_PW = 6
    isDebug = True;
    isRelease = True;
