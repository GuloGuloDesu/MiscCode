package com.gulo;

public class Main {
    public static void main(String[] args) {

        /* 3rd program */
        // int has a width of 32
        int myMinValue = -2_147_483_648;
        int myMaxValue = 2_147_483_647;
        int myTotal = (myMinValue / 2);
        System.out.println("myTotal = " + myTotal);

        // byte has a width of 8
        byte myByteValue = 127;
        byte myNewByteValue = (byte) (myByteValue / 2);
        System.out.println("myNewByteValue = " + myNewByteValue);

        // short has a width of 16
        short myShortValue = 32767;
        short myNewShortValue = (short) (myShortValue / 2 );
        System.out.println("myNewShortValue = " + myNewShortValue);

        // long has a width of 64
        long myLongValue = 9_223_372_036_854_775_807L;


        /* 3rd progam challenge */
        byte myByte = 127;
        short myShort = 8008;
        int myInt = 80085;
        long myLong = 50_000L + (10L * (myByte + myShort + myInt));
        System.out.println("myLong = " + myLong);

    }
}
