// qmargins.sip generated by MetaSIP
//
// This file is part of the QtCore Python extension module.
//
// Copyright (c) 2016 Riverbank Computing Limited <info@riverbankcomputing.com>
// 
// This file is part of PyQt4.
// 
// This file may be used under the terms of the GNU General Public License
// version 3.0 as published by the Free Software Foundation and appearing in
// the file LICENSE included in the packaging of this file.  Please review the
// following information to ensure the GNU General Public License version 3.0
// requirements will be met: http://www.gnu.org/copyleft/gpl.html.
// 
// If you do not wish to use this file under the terms of the GPL version 3.0
// then you may purchase a commercial license.  For more information contact
// info@riverbankcomputing.com.
// 
// This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
// WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


%If (Qt_4_6_0 -)

class QMargins
{
%TypeHeaderCode
#include <qmargins.h>
%End

public:
    QMargins();
    QMargins(int aleft, int atop, int aright, int abottom);
    bool isNull() const;
    int left() const;
    int top() const;
    int right() const;
    int bottom() const;
    void setLeft(int aleft);
    void setTop(int atop);
    void setRight(int aright);
    void setBottom(int abottom);
};

%End
%If (Qt_4_6_0 -)
bool operator==(const QMargins &m1, const QMargins &m2);
%End
%If (Qt_4_6_0 -)
bool operator!=(const QMargins &m1, const QMargins &m2);
%End
%If (Qt_5_0_0 -)
QDataStream &operator<<(QDataStream &, const QMargins & /Constrained/);
%End
%If (Qt_5_0_0 -)
QDataStream &operator>>(QDataStream &, QMargins & /Constrained/);
%End
