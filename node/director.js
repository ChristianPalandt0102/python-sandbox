const net = require("net");

const PYTHON_CORE = 9000;

const server = net.createServer(socket => {

    const backend = net.connect(PYTHON_CORE);

    socket.pipe(backend);
    backend.pipe(socket);

});

server.listen(8000, () =>
    console.log("Director router running")
);
