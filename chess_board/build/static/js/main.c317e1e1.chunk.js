(this.webpackJsonpchess_board=this.webpackJsonpchess_board||[]).push([[0],{20:function(e,t,a){},36:function(e,t,a){},37:function(e,t,a){},58:function(e,t,a){},67:function(e,t,a){"use strict";a.r(t);for(var c=a(0),n=a.n(c),i=a(29),o=a.n(i),s=(a(36),a(4)),l=a(10),r=a(11),d=a(14),u=a(13),f=(a(37),a(1)),p=function(e){return e.number%2===0?Object(f.jsx)("div",{className:"tile black-tile",children:e.image&&Object(f.jsx)("div",{style:{backgroundImage:"url(".concat(e.image,")")},className:"chess-piece"})}):Object(f.jsx)("div",{className:"tile white-tile",children:e.image&&Object(f.jsx)("div",{style:{backgroundImage:"url(".concat(e.image,")")},className:"chess-piece"})})},b=(a(20),function(e){return Object(f.jsx)("div",{id:"chessboard",children:e.board})}),h=function(e){Object(d.a)(a,e);var t=Object(u.a)(a);function a(){var e;Object(l.a)(this,a);for(var c=arguments.length,n=new Array(c),i=0;i<c;i++)n[i]=arguments[i];return(e=t.call.apply(t,[this].concat(n))).mode=function(){return 0===e.props.mode?"F\xe1cil":1===e.props.mode?"Medio":"Dif\xedcil"},e}return Object(r.a)(a,[{key:"render",value:function(){return Object(f.jsx)("div",{children:Object(f.jsxs)("div",{className:"row",children:[Object(f.jsx)("div",{className:"col s12",children:Object(f.jsxs)("h4",{className:"white-text center",children:["Dificultad actual: ",this.mode()]})}),Object(f.jsx)("div",{className:"input-field col s12 center",children:Object(f.jsx)("input",{type:"button",value:"F\xe1cil",className:"waves-effect waves-ligh btn blue accent-3",onClick:this.props.onClick})}),Object(f.jsx)("div",{className:"input-field col s12 center",children:Object(f.jsx)("input",{type:"button",value:"Medio",className:"waves-effect waves-ligh btn blue accent-3",onClick:this.props.onClick})}),Object(f.jsx)("div",{className:"input-field col s12 center",children:Object(f.jsx)("input",{type:"button",value:"Dif\xedcil",onClick:this.props.onClick,className:"waves-effect waves-ligh btn blue accent-3"})}),Object(f.jsx)("div",{className:"input-field col s12 center",children:Object(f.jsx)("input",{type:"button",value:"PC vs PC",className:"waves-effect waves-ligh btn red accent-3",onClick:this.props.onClick})})]})})}}]),a}(c.Component),g=a(15),m=a.n(g),v="http://localhost:8000/chess",j=function(){function e(){Object(l.a)(this,e)}return Object(r.a)(e,[{key:"getStart",value:function(){var e="".concat(v,"/");return m.a.get(e).then((function(e){return e.data}))}},{key:"movimiento",value:function(e,t){var a="".concat(v,"/").concat(e,"/").concat(t);return m.a.get(a).then((function(e){return e.data}))}},{key:"automatic_move",value:function(e){var t="".concat(v,"/").concat(e);return m.a.get(t).then((function(e){return e.data}))}}]),e}(),O=a.p+"static/media/chess-pawn-black.a90021bc.png",x=a.p+"static/media/chess-pawn-white.ebae9f48.png",y=a.p+"static/media/chess-rook-black.d6fa7518.png",k=a.p+"static/media/chess-rook-white.58159299.png",w=a.p+"static/media/chess-knight-black.f3906ab1.png",P=a.p+"static/media/chess-knight-white.e0fa4264.png",N=a.p+"static/media/chess-bishop-black.5940250f.png",C=a.p+"static/media/chess-bishop-white.311e0daa.png",M=a.p+"static/media/chess-king-black.d2a1a7e6.png",S=a.p+"static/media/chess-king-white.bcf06732.png",T=a.p+"static/media/chess-queen-black.0af97291.png",I=a.p+"static/media/chess-queen-white.25cde828.png",X=new j,Y=[1,2,3,4,5,6,7,8],L=["a","b","c","d","e","f","g","h"],_={a:0,b:1,c:2,d:3,e:4,f:5,g:6,h:7,1:0,2:1,3:2,4:3,5:4,6:5,7:6,8:7},D="PAWN",E="BISHOP",U="KNIGHT",A="ROOK",B="QUEEN",F="KING",H=[],J=0;J<2;J++){var W=0===J?"black":"white",K=0===J?7:0;H.push({image:"black"===W?y:k,x:0,y:K,type:A},{image:"black"===W?y:k,x:7,y:K,type:A},{image:"black"===W?w:P,x:1,y:K,type:U},{image:"black"===W?w:P,x:6,y:K,type:U},{image:"black"===W?N:C,x:2,y:K,type:E},{image:"black"===W?N:C,x:5,y:K,type:E},{image:"black"===W?M:S,x:4,y:K,type:F},{image:"black"===W?T:I,x:3,y:K,type:B})}for(var q=0;q<8;q++)H.push({image:O,x:q,y:6,type:D}),H.push({image:x,x:q,y:1,type:D});var z=function(e){Object(d.a)(a,e);var t=Object(u.a)(a);function a(){var e;Object(l.a)(this,a),(e=t.call(this)).board=[],e.state={pieces:H,gridX:0,gridY:0,originalX:0,originalY:0,offsetLeft:0,offsetTop:0,clientWidth:0,clientHeight:0,activePiece:null,to_x:-1,to_y:-1,mode:0,pc:[0,2],gameState:0},e.ponerTablero=function(){e.board=[];for(var t=function(t){for(var a=function(a){var c=a+t+2,n=void 0;e.state.pieces.forEach((function(e){e.x===a&&e.y===t&&(n=e.image)})),e.board.push(Object(f.jsx)(p,{number:c,image:n},"".concat(t,",").concat(a)))},c=0;c<L.length;c++)a(c)},a=Y.length-1;a>=0;a--)t(a)},e.componentDidMount=function(t){e.setState(Object(s.a)(Object(s.a)({},e.state),{},{offsetLeft:document.getElementById("chessboard").offsetLeft,offsetTop:document.getElementById("chessboard").offsetTop,clientWidth:document.getElementById("chessboard").clientWidth,clientHeight:document.getElementById("chessboard").clientHeight})),X.getStart().then((function(t){e.setState(Object(s.a)(Object(s.a)({},e.state),{},{gameState:t.status})),console.log(t,e.state)}))},e.activePiece=null,e.grabPiece=function(t){var a=t.target;if(a.classList.contains("chess-piece")){var c=Math.floor((t.clientX-e.state.offsetLeft)/60),n=Math.abs(Math.ceil((t.clientY-e.state.offsetTop-480)/60));console.log(c,n),e.setState(Object(s.a)(Object(s.a)({},e.state),{},{gridX:c,gridY:n,originalX:c,originalY:n}));var i=t.clientX-30,o=t.clientY-30;a.style.position="absolute",a.style.left="".concat(i,"px"),a.style.top="".concat(o,"px"),e.activePiece=a}},e.movePiece=function(t){if(e.activePiece){var a=e.state.offsetLeft-15,c=e.state.offsetTop-15,n=e.state.offsetLeft+e.state.clientWidth-45,i=e.state.offsetTop+e.state.clientHeight-45,o=t.clientX-30,s=t.clientY-30;e.activePiece.style.position="absolute",e.activePiece.style.left="".concat(o<a?a:o>n?n:o,"px"),e.activePiece.style.top="".concat(s<c?c:s>i?i:s,"px")}},e.sleep=function(e){var t=Date.now(),a=null;do{a=Date.now()}while(a-t<e)},e.dropPiece=function(t){var a=-1,c=-1;if(e.activePiece){a=Math.floor((t.clientX-e.state.offsetLeft)/60),c=Math.abs(Math.ceil((t.clientY-e.state.offsetTop-480)/60));var n=""+L[e.state.gridX]+Y[e.state.gridY]+L[a]+Y[c];console.log(n),X.movimiento(n,e.state.mode).then((function(t){console.log(t),t.isValid?(e.state.pieces.map((function(t){return t.x===e.state.gridX&&t.y===e.state.gridY&&(t.x=a,t.y=c),t})),e.ponerTablero(),e.forceUpdate(),e.sleep(1e3),e.movePieceAlone(t.move)):(console.log("falso"),e.state.pieces.map((function(t){return t.x===e.state.gridX&&t.y===e.state.gridY&&(t.x=a,t.y=c,console.log(t),console.log(e.state)),t})),e.ponerTablero(),e.forceUpdate(),e.state.pieces.map((function(t){return t.x===a&&t.y===c&&(t.x=e.state.originalX,t.y=e.state.originalY,console.log(t)),t})),e.ponerTablero(),e.forceUpdate(),alert("Moimiento Inv\xe1lido")),e.ponerTablero(),e.forceUpdate()})),e.activePiece=null}},e.handleClickMode=function(t){var a=t.target.value;"PC vs PC"!==a?"F\xe1cil"===a?e.setState(Object(s.a)(Object(s.a)({},e.state),{},{mode:0})):"Medio"===a?e.setState(Object(s.a)(Object(s.a)({},e.state),{},{mode:1})):e.setState(Object(s.a)(Object(s.a)({},e.state),{},{mode:2})):e.automatic_game()},e.cont_moves=0,e.automatic_game=function(){if("gameOver"!==e.state.gameState){var t=e.cont_moves%2;console.log(t),console.log(e.state.pc[t]),X.automatic_move(e.state.pc[t]).then((function(t){console.log(t),e.setState(Object(s.a)(Object(s.a)({},e.state),{},{gameState:t.status})),e.movePieceAlone(t.move),e.cont_moves++})),e.ponerTablero(),e.forceUpdate()}else e.finalizarJuego()},e.movePieceAlone=function(t){var a=_[t[2]],c=_[t[3]],n=[];e.state.pieces.map((function(e){e.x===a&&e.y===c?(console.log("ADIOS"),console.log(e)):(console.log("HOLA"),n.push(e))})),e.setState(Object(s.a)(Object(s.a)({},e.state),{},{pieces:n})),e.ponerTablero(),e.forceUpdate(),e.state.pieces.map((function(e){return e.x===_[t[0]]&&e.y===_[t[1]]&&(e.x=a,e.y=c),e})),e.ponerTablero(),e.forceUpdate()},e.finalizarJuego=function(){alert("Juego terminado, la p\xe1gina se recargar\xe1 en 5 segundos"),e.sleep(5e3),e.location.reload()};for(var c=function(t){for(var a=function(a){var c=a+t+2,n=void 0;e.state.pieces.forEach((function(e){e.x===a&&e.y===t&&(n=e.image)})),e.board.push(Object(f.jsx)(p,{number:c,image:n},"".concat(t,",").concat(a)))},c=0;c<L.length;c++)a(c)},n=Y.length-1;n>=0;n--)c(n);return e}return Object(r.a)(a,[{key:"render",value:function(){var e=this;return Object(f.jsxs)("div",{className:"row",children:[Object(f.jsx)("div",{className:"col s8",id:"app",children:Object(f.jsx)("div",{id:"chessboard",onMouseMove:function(t){return e.movePiece(t)},onMouseDown:function(t){return e.grabPiece(t)},onMouseUp:function(t){return e.dropPiece(t)},children:Object(f.jsx)(b,{board:this.board})})}),Object(f.jsx)("div",{className:"col s4",id:"dificultad",children:Object(f.jsx)(h,{mode:this.state.mode,onClick:this.handleClickMode})})]})}}]),a}(c.Component),G=a(30),Q=a(2);a(57),a(58);var R=function(){return Object(f.jsx)(G.a,{children:Object(f.jsx)(Q.a,{path:"/",exact:!0,component:z})})},V=function(e){e&&e instanceof Function&&a.e(3).then(a.bind(null,68)).then((function(t){var a=t.getCLS,c=t.getFID,n=t.getFCP,i=t.getLCP,o=t.getTTFB;a(e),c(e),n(e),i(e),o(e)}))};o.a.render(Object(f.jsx)(n.a.StrictMode,{children:Object(f.jsx)(R,{})}),document.getElementById("root")),V()}},[[67,1,2]]]);
//# sourceMappingURL=main.c317e1e1.chunk.js.map