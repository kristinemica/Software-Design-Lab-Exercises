ListNode xprev = L.header;
ListNode yprev = L.header;

if( x == y ) {
    return;
}
while(( x_prev != null )&&( x_prev.getNext() != x )) {
    x_prev = x_prev.getNext();
}
while(( y_prev != null )&&( y_prev.getNext() != y )) {
    y_prev = y_prev.getNext();
}
if(( x_prev == null )||( y_prev == null )) {
    throw new NodeNotFoundException();
}
if( y_prev == x ) {

    x.setNext( y.getNext());
    y.setNext( x );
    x_prev.setNext( y );
}
else if( x_prev == y ) {

    y.setNext( x.getNext());
    x.setNext( y );
    y_prev.setNext( x );
}
else {
    Node tmp = x.getNext();
    x.setNext( y.getNext());
    y.setNext( tmp );

    x_prev.setNext( y );
    y_prev.setNext( x );
}
