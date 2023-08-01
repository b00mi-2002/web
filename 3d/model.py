import numpy as np

class Triangle:
    def __init__(self,app):
        self.app = app
        self.ctx = app.ctx
        self.vbo=self.get_vbo()
        self.shader_program=self.get_shader_program('default')
        self.vao = self.get_vao()

    def render(self):
        self.vao.render()
    
    def destroy(self):
        self.vbo.release()
        self.shader_program.release()
        self.vao.release()

    def get_vao(self):
        vao = self.ctx.vertex_array(self.shader_program, [(self.vbo, '3f', 'in_position')])
        return vao


    def get_vertex_data(self):
        vertex_data =[(-0.6, -0.8, 0.0), (0.6, -0.8, 0.0), (0.0,0.8,0.0)]
        vertex_data = np.array(vertex_data,dtype='f4')

    def get_vbo(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo
    
    def get_shader_program(self,shader_name):
        with open(f'shaders/{shader_name}.vert') as file:
            vertex_shader =file.read()

        with open(f'shaders/{shader_name}.frag') as file:
            fragment_shader = file.read()

        program = self.ctx.program(vertex_shader=vertex_shader,fragment_shader=fragment_shader)
        return program