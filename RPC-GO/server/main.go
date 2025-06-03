package main

import (
	"context"
	"log"
	"net"

	"google.golang.org/grpc"
	pb "rpc/generated" 
)

type server struct {
	pb.UnimplementedAdderServer
}

func (s *server) Add(ctx context.Context, req *pb.AddRequest) (*pb.AddResponse, error) {
	return &pb.AddResponse{Result: req.A + req.B}, nil
}

func main() {
	lis, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatalf("Failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterAdderServer(s, &server{})
	log.Println("gRPC Server running on port 50051...")
	s.Serve(lis)
}