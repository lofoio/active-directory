package main
import ("net";"container/vector";"bufio";"strings")
type client struct { conn net.Conn; send chan string; receive chan string }
func main() {
    if listener, err := net.Listen("tcp", "0.0.0.0:4242"); err == nil {
    	master := make(chan string, 100);
    	clients := vector.New(0);
    	go runServer(master, clients);
    	for {
    		if conn, err := listener.Accept(); err == nil {
    			c := client{ conn, master, make(chan string, 100) };
    			clients.Push(c);
    			go runClient(c);
    		} else { break } } } }
func runServer(master chan string, clients *vector.Vector) {
    for {
    	message := <-master;
    	clients.Do(func (c interface{}) { c.(client).receive <- message }); } }
func runClient(c client) {
    input := make(chan string, 10);
    go readLines(c, input);
    for {
    	select {
    	case inMessage := <-input: c.send <- inMessage;
    	case outMessage := <-c.receive: c.conn.Write(strings.Bytes(outMessage));
    	} } }
func readLines(c client, input chan string) {
    reader := bufio.NewReader(c.conn);
    for { if line, err := reader.ReadString('\n'); err == nil
    		{ input <- line; } else { break } } }