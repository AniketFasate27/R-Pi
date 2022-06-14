// Example testing sketch for various DHT humidity/temperature sensors written by ladyada
// REQUIRES the following Arduino libraries:
// - DHT Sensor Library: https://github.com/adafruit/DHT-sensor-library
// - Adafruit Unified Sensor Lib: https://github.com/adafruit/Adafruit_Sensor

#include "DHT.h"

#define DHTPIN 15     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321
DHT dht(DHTPIN, DHTTYPE);
int i = 1;
int chipid;
char id_[6];
char id_1[10];
char kid[12];
char k_id[12];
String device_id;
void setup() {
  Serial.begin(115200);
  //Serial.println(F("DHTxx test!"));

  dht.begin();
  chipid = ESP.getEfuseMac(); //The chip ID is essentially its MAC address(length: 6 bytes).
  sprintf(id_, "%04X", (uint16_t)(chipid >> 32));
  sprintf(id_1, "%08X\n", (uint32_t)chipid);
  strcat(kid, id_);
  strcat(kid, id_1);
  sprintf(k_id, "%c%c%c%c%c%c%c%c%c%c%c%c", kid[10], kid[11], kid[8], kid[9], kid[6], kid[7], kid[4], kid[5], kid[2], kid[3], kid[0], kid[1]);//k_id is the ssid name of AP
  Serial.println(k_id);
  device_id = String(k_id);

  
}

void loop() {
  // Wait a few seconds between measurements.

  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(f, h);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);


  Serial.print(device_id);
  Serial.print(',');
  Serial.print(h);
  Serial.print(',');
  Serial.print(t);
  Serial.print(',');
  Serial.print(f);
  Serial.print(',');
  Serial.print(hic);
  Serial.print('\n');
  i = i + 1;
  delay(60000);
  //  Serial.print(F("Humidity: "));
  //  Serial.print(h);
  //  Serial.print(F("%  Temperature: "));
  //  Serial.print(t);
  //  Serial.print(F("°C "));
  //  Serial.print(f);
  //  Serial.print(F("°F  Heat index: "));
  //  Serial.print(hic);
  //  Serial.print(F("°C "));
  //  Serial.print(hif);
  //  Serial.println(F("°F"));
}
