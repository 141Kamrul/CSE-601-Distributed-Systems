go mod init rpc

protoc --go_out=./generated --go-grpc_out=./generated adder.proto

go install google.golang.org/protobuf/cmd/protoc-gen-go@latest 
go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
go install google.golang.org/grpc

