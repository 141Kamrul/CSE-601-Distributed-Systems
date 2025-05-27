package main

import (
	"context"
	"log"

	"google.golang.org/grpc"
	pb "rpc/generated" 
)

func main() {
	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("Failed to connect: %v", err)
	}
	defer conn.Close()

	client := pb.NewAdderClient(conn)
	res, err := client.Add(context.Background(), &pb.AddRequest{A: 10, B: 3})
	if err != nil {
		log.Fatalf("Failed to call Add: %v", err)
	}
	log.Printf("Result: %d", res.Result) 
}