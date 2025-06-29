package com.javasim.teste.basic;

import org.javasim.RestartException;
import org.javasim.Simulation;
import org.javasim.SimulationException;
import org.javasim.SimulationProcess;

public class Controle extends SimulationProcess
{


    public static double tempoRespostaTotal = 0.0;
    public static long totalClientes = 0;
    public static long clientesProcessados = 0;
    public static double totalServico = 0;


    public Controle()
    {
        
    }

    public void run ()
    {
        try
        {
