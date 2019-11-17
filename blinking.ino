int LED=13;
String data;
int led2=12;
int val=0;
void setup() {
  // put your setup code here, to run once:
  pinMode(LED,OUTPUT);
  pinMode(led2,OUTPUT);
  Serial.begin(9600);
  

}

void loop() {
  while (Serial.available()){
      data = Serial.readString();
      val= data.toInt();
   }
  // put your main code here, to run repeatedly:
  Serial.println(val);
  if(val==1){
    digitalWrite(LED,HIGH);
    digitalWrite(led2,HIGH);
    delay(1000);
  }

  else{
    digitalWrite(led2,LOW);
    digitalWrite(LED,LOW);
    delay(1000);
    }
  }
