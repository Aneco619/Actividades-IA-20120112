var w=800;
var h=400;
var jugador;
var fondo;

// estas variables son las de las balas que salen de las naves
var bala, bala1 , balaD=false,balaD1= false, nave;

//variables para el salto, despliegue menu, movimiento izquierda y derecha del personaje
var salto;
var menu;
var izquierda;
var derecha;
var saltosonido;

//  bala de la primer y segunda nave
var velocidadBala, velocidadBala1;
var despBala, despBala1;
var estatusAire;
var estatuSuelo;

var nnNetwork , nnEntrenamiento, nnSalida, datosEntrenamiento=[];
var modoAuto = false, eCompleto=false;



var juego = new Phaser.Game(w, h, Phaser.CANVAS, '', { preload: preload, create: create, update: update, render:render});

function preload() {
    juego.load.image('fondo', 'assets/game/fondo.jpg');
    juego.load.spritesheet('mono', 'assets/sprites/altair.png',32 ,48);
    juego.load.image('nave', 'assets/game/ufo.png');
    juego.load.image('bala', 'assets/sprites/purple_ball.png');
    juego.load.image('menu', 'assets/game/menu.png');

}



function create() {

    juego.physics.startSystem(Phaser.Physics.ARCADE);
    juego.physics.arcade.gravity.y = 800;
    juego.time.desiredFps = 30;

    fondo = juego.add.tileSprite(0, 0, w, h, 'fondo');
    nave = juego.add.sprite(w-100, h-70, 'nave');
    nave1 = juego.add.sprite(w-750, h-390, 'nave'); //la nave que dispara en vertical, hacía abajo
    bala = juego.add.sprite(w-100, h, 'bala');
    bala1 = juego.add.sprite(w-715, h-350, 'bala'); 
    jugador = juego.add.sprite(50, h, 'mono');


    //encargado de la animación correr
    juego.physics.enable(jugador);
    jugador.body.collideWorldBounds = true;
    var corre = jugador.animations.add('corre',[8,9,10,11]);
    jugador.animations.play('corre', 10, true);

   
    juego.physics.enable(bala);
    bala.body.collideWorldBounds = true;

   
    juego.physics.enable(bala1);
    bala1.body.collideWorldBounds = true;

    pausaL = juego.add.text(w - 100, 20, 'Pausa', { font: '20px Arial', fill: '#fff' });
    pausaL.inputEnabled = true;
    pausaL.events.onInputUp.add(pausa, self);
    juego.input.onDown.add(mPausa, self);

    // asignamos el salto, el movimiento a la izquierda y derecha a las teclas en nuestro teclado, las cuales son, el espacio, flecha izquierda y derecha
    salto = juego.input.keyboard.addKey(Phaser.Keyboard.SPACEBAR);
    izquierda = juego.input.keyboard.addKey(Phaser.Keyboard.LEFT);
    derecha = juego.input.keyboard.addKey(Phaser.Keyboard.RIGHT);

    
    nnNetwork =  new synaptic.Architect.Perceptron(2, 6, 6, 2);
    nnEntrenamiento = new synaptic.Trainer(nnNetwork);

}

function enRedNeural(){
    nnEntrenamiento.train(datosEntrenamiento, {rate: 0.0003, iterations: 10000, shuffle: true});
}


function datosDeEntrenamiento(param_entrada){

    console.log("Entrada",param_entrada[0]+" "+param_entrada[1]);
    nnSalida = nnNetwork.activate(param_entrada);
    var aire=Math.round( nnSalida[0]*100 );
    var piso=Math.round( nnSalida[1]*100 );
    console.log("Valor ","En el Aire %: "+ aire + " En el suelo %: " + piso );
    console.log("Datos de Entrenamiento: ", datosEntrenamiento);
    return nnSalida[0]>=nnSalida[1];
}



function pausa(){
    juego.paused = true;
    menu = juego.add.sprite(w/2,h/2, 'menu');
    menu.anchor.setTo(0.5, 0.5);
    jugador.body.velocity.x=0;
    jugador.body.velocity.y=0;
    jugador.position.x=50;
}

function mPausa(event){
    if(juego.paused){
        var menu_x1 = w/2 - 270/2, menu_x2 = w/2 + 270/2,
            menu_y1 = h/2 - 180/2, menu_y2 = h/2 + 180/2;

        var mouse_x = event.x  ,
            mouse_y = event.y  ;

        if(mouse_x > menu_x1 && mouse_x < menu_x2 && mouse_y > menu_y1 && mouse_y < menu_y2 ){
            if(mouse_x >=menu_x1 && mouse_x <=menu_x2 && mouse_y >=menu_y1 && mouse_y <=menu_y1+90){
                eCompleto=false;
                datosEntrenamiento = [];
                modoAuto = false;
            }else if (mouse_x >=menu_x1 && mouse_x <=menu_x2 && mouse_y >=menu_y1+90 && mouse_y <=menu_y2) {
                if(!eCompleto) {
                    console.log("","Entrenamiento "+ datosEntrenamiento.length +" valores" );
                    enRedNeural();
                    eCompleto=true;
                }
                modoAuto = true;
            }

            menu.destroy();
            resetVariables();
            juego.paused = false;

        }
    }
}


function resetVariables(){
    jugador.body.velocity.x=0;
    jugador.body.velocity.y=0;
    bala.body.velocity.x = 0;
    bala.position.x = w-100;
    jugador.position.x=50;
    balaD=false;
}


function saltar(){
    jugador.body.velocity.y = -270;
}


function update() {

    fondo.tilePosition.x -= 1; 

    juego.physics.arcade.collide(bala, jugador, colisionH, null, this);

    estatuSuelo = 1;
    estatusAire = 0;

    if(!jugador.body.onFloor()) {
        estatuSuelo = 0;
        estatusAire = 1;
    }
    
	
    despBala = Math.floor( jugador.position.x - bala.position.x );

    // Verificamos si estamos en el modo manual y alguna tecla está presionada
    if (modoAuto == false) {
        if (salto.isDown && jugador.body.onFloor()) {
            saltar();
        } else if (izquierda.isDown && jugador.body.onFloor()) {
            movIzquierda();
        } else if (derecha.isDown && jugador.body.onFloor()) {
            movDerecha();
        }
    } else {  // En modo automático
        // Verificamos si las balas están en juego y el jugador está en el suelo
        if (modoAuto == true && bala.position.x > 0 && bala1.position.x > 0 && jugador.body.onFloor()) {
            if (datosDeEntrenamiento([despBala, velocidadBala, despBala1, velocidadBala1])) {
                if (Math.random() < 0.5) {
                    movIzquierda();
                } else {
                    movDerecha();
                }
                saltar();
            }
        }
    }

    if( balaD==false ){
        disparo();
    }

    if( bala.position.x <= 0  ){
        resetVariables();
    }
    
    if( modoAuto ==false  && bala.position.x > 0 ){

        datosEntrenamiento.push({
                'input' :  [despBala , velocidadBala],
                'output':  [estatusAire , estatuSuelo ]  
        });

        console.log("Desplazamiento Bala, Velocidad Bala, Estatus, Estatus: ",
            despBala + " " +velocidadBala + " "+ estatusAire+" "+  estatuSuelo);
   }

}

//reestablecer el estado del muñeco, la bala en horizontal
function resetVariables(){
    jugador.body.velocity.x=0;
    jugador.body.velocity.y=0;
    bala.body.velocity.x = 0;
    bala.position.x = w-100;
    balaD=false;
    resetJugador();
}

//reestablecer el estado del muñeco, la bala en vertical
function resetVariables1(){
    jugador.body.velocity.x=0;
    jugador.body.velocity.y=0;
    bala1.body.velocity.y = 0;
    bala1.position.y = nave1.position.y;
    balaD1=false;
    resetJugador();
}

//aquí es la función que nos permite saltar y aparte agregamos la de la acción de cuando el muñeco se mueve a la izquierda y a la derecha, con el manejo del parametro
// velocity en el eje y puesto que el muñeco salta hacia arriba y los del movimiento en izquierda es negativo porque se mueve para atras y positivo para cuando se mueve hacia en frente

function saltar(){
    jugador.body.velocity.y = -270;
}
function movIzquierda(){
    jugador.body.velocity.x = -120;
}
function movDerecha(){
    jugador.body.velocity.x = 100;
}



// aquí la función del disparo que realiza la nave
function disparo(){
    velocidadBala =  -1 * velocidadRandom(200,600);
    bala.body.velocity.y = 0 ;
    bala.body.velocity.x = velocidadBala ;
    balaD=true;
}

//lo mismo para la otra nave
function disparo1(){
    velocidadBala1 =  -0.1 * velocidadRandom(700,700);
    bala1.body.velocity.x = 0 ;
    bala1.body.velocity.y = velocidadBala1;
    balaD1=true;
}

//la función colisionh que es la que detiene todos
function colisionH(){
    pausa();
}

function velocidadRandom(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function render(){

}

function resetJugador() {
    jugador.position.x = 50;
    jugador.position.y = h;
    jugador.body.velocity.x = 0;
    jugador.body.velocity.y = 0;
}