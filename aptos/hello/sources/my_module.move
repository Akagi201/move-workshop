module hello::my_module {
    use std::string;

    public fun speak(): string::String {
        string::utf8(b"Hello World")
    }

    #[test]
    public fun test_speak() {
        use std::debug;
        let res = speak();

        debug::print(&res);

        let except = string::utf8(b"Hello World");
        assert!(res == except, 0);
    }
}