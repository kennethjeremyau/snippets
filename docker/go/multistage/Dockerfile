FROM golang:alpine AS builder
WORKDIR /app
COPY /app .
RUN go mod tidy \
    && go build -o /build main.go


FROM alpine
WORKDIR /
COPY --from=builder /build /app
ENTRYPOINT ["/app"]
