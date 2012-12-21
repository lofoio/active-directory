package main
import ("image"; "image/png"; "math"; "bufio"; "os"; "time")
const clock_size = 200;
const radius = clock_size / 3;
var colour image.RGBAColor;
func circle (clock *image.RGBA) {
    for angle := float64(0); angle < 360; angle++ {
        radian_angle := math.Pi * 2 * angle / 360;
        x := radius * math.Sin (radian_angle) + clock_size/2;
        y := radius * math.Cos (radian_angle) + clock_size/2;
        clock.Set (int (x), int (y), colour);}}
func hand (clock *image.RGBA, angle float64, length float64) {
    radian_angle := math.Pi * 2 * angle;
    x_inc := math.Sin (radian_angle);
    y_inc := -math.Cos (radian_angle);
    for i := float64(0); i < length; i++ {
        x := i * x_inc + clock_size/2;
        y := i * y_inc + clock_size/2;
        clock.Set (int (x), int (y), colour);}}
func main () {
    clock := image.NewRGBA (clock_size, clock_size);
    colour.A = 255;
    circle (clock);
    time := time.LocalTime ();
    hand (clock, (float64(time.Hour) + float64(time.Minute)/60)/12, radius*0.6); // hour hand
    hand (clock, (float64(time.Minute) + float64(time.Second)/60)/60, radius*0.8); // minute hand
    out := bufio.NewWriter(os.Stdout);
    defer out.Flush();
    png.Encode(out, clock);
}